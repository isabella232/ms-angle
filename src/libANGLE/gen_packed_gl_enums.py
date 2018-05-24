# Copyright 2018 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# gen_packed_gl_enums.py:
#  Code generation for the packed enums.

import datetime, json, os, sys
from collections import namedtuple

Enum = namedtuple('Enum', ['name', 'values', 'max_value'])
EnumValue = namedtuple('EnumValue', ['name', 'gl_name', 'value'])

Generators = [
    {
        'json': 'packed_gl_enums.json',
        'output': 'PackedGLEnums',
        'namespace': 'gl',
        'enum_type': 'GLenum',
    },
    {
        'json': 'packed_egl_enums.json',
        'output': 'PackedEGLEnums',
        'namespace': 'egl',
        'enum_type': 'EGLenum',
    },
]

def load_enums(path):
    with open(path) as map_file:
        enums_dict = json.loads(map_file.read())

    enums = []
    for (enum_name, value_list) in enums_dict.iteritems():

        if isinstance(value_list, dict):
            values = []
            i = 0
            for (value_name, value_gl_name) in sorted(value_list.iteritems()):
                values.append(EnumValue(value_name, value_gl_name, i))
                i += 1

            assert(i < 255) # This makes sure enums fit in the uint8_t
            enums.append(Enum(enum_name, values, i))

        else:
            assert(isinstance(value_list, list))

            values = [EnumValue(v['name'], v['gl_name'], v['value']) for v in value_list]
            max_value = max([value.value for value in values]) + 1

            enums.append(Enum(enum_name, values, max_value))

    enums.sort(key=lambda enum: enum.name)
    return enums

def generate_include_guard(path):
    return path.replace(".", "_").upper()

def header_name_from_cpp_name(path):
    return path.replace(".cpp", ".h")

header_template = """// GENERATED FILE - DO NOT EDIT.
// Generated by {script_name} using data from {data_source_name}.
//
// Copyright {copyright_year} The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//
// {file_name}:
//   Declares ANGLE-specific enums classes for {api_enum_name}s and functions operating
//   on them.

#ifndef LIBANGLE_{include_guard}_
#define LIBANGLE_{include_guard}_

#include <angle_gl.h>
#include <EGL/egl.h>
#include <EGL/eglext.h>

#include <cstdint>

namespace {namespace}
{{

template<typename Enum>
Enum From{api_enum_name}({api_enum_name} from);
{content}
}}  // namespace {namespace}

#endif // LIBANGLE_{include_guard}_
"""

enum_declaration_template = """
enum class {enum_name} : uint8_t
{{
{value_declarations}

    InvalidEnum = {max_value},
    EnumCount = {max_value},
}};

template <>
{enum_name} From{api_enum_name}<{enum_name}>({api_enum_name} from);
{api_enum_name} To{api_enum_name}({enum_name} from);
"""

def write_header(enums, path_prefix, file_name, data_source_name, namespace, api_enum_name):
    content = ['']

    for enum in enums:
        value_declarations = []
        for value in enum.values:
            value_declarations.append('    ' + value.name + ' = ' + str(value.value) + ',')

        content.append(enum_declaration_template.format(
            enum_name = enum.name,
            max_value = str(enum.max_value),
            value_declarations = '\n'.join(value_declarations),
            api_enum_name = api_enum_name
        ))

    header = header_template.format(
        content = ''.join(content),
        copyright_year = datetime.date.today().year,
        data_source_name = data_source_name,
        script_name = sys.argv[0],
        file_name = file_name,
        include_guard = generate_include_guard(file_name),
        namespace = namespace,
        api_enum_name = api_enum_name
    )

    with (open(path_prefix + file_name, 'wt')) as f:
        f.write(header)

cpp_template = """// GENERATED FILE - DO NOT EDIT.
// Generated by {script_name} using data from {data_source_name}.
//
// Copyright {copyright_year} The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//
// {file_name}:
//   Implements ANGLE-specific enums classes for {api_enum_name}s and functions operating
//   on them.

#include "common/debug.h"
#include "libANGLE/{header_name}"

namespace {namespace}
{{
{content}
}}  // namespace {namespace}
"""

enum_implementation_template = """
template <>
{enum_name} From{api_enum_name}<{enum_name}>({api_enum_name} from)
{{
    switch (from)
    {{
{from_glenum_cases}
        default:
            return {enum_name}::InvalidEnum;
    }}
}}

{api_enum_name} To{api_enum_name}({enum_name} from)
{{
    switch (from)
    {{
{to_glenum_cases}
        default:
            UNREACHABLE();
            return 0;
    }}
}}
"""

def write_cpp(enums, path_prefix, file_name, data_source_name, namespace, api_enum_name):
    content = ['']

    for enum in enums:
        from_glenum_cases = []
        to_glenum_cases = []
        for value in enum.values:
            qualified_name = enum.name + '::' + value.name
            from_glenum_cases.append('        case ' + value.gl_name + ':\n            return ' + qualified_name + ';')
            to_glenum_cases.append('        case ' + qualified_name + ':\n            return ' + value.gl_name + ';')

        content.append(enum_implementation_template.format(
            enum_name = enum.name,
            from_glenum_cases = '\n'.join(from_glenum_cases),
            max_value = str(enum.max_value),
            to_glenum_cases = '\n'.join(to_glenum_cases),
            api_enum_name = api_enum_name
        ))

    cpp = cpp_template.format(
        content = ''.join(content),
        copyright_year = datetime.date.today().year,
        data_source_name = data_source_name,
        script_name = sys.argv[0],
        file_name = file_name,
        header_name = header_name_from_cpp_name(file_name),
        namespace = namespace,
        api_enum_name = api_enum_name
    )

    with (open(path_prefix + file_name, 'wt')) as f:
        f.write(cpp)

if __name__ == '__main__':
    path_prefix = os.path.dirname(os.path.realpath(__file__)) + os.path.sep

    for generator in Generators:
        json_file = generator['json']
        output_file = generator['output']
        namespace = generator['namespace']
        enum_type = generator['enum_type']
        enums = load_enums(path_prefix + json_file)
        write_header(enums, path_prefix, output_file + '_autogen.h', json_file, namespace, enum_type)
        write_cpp(enums, path_prefix, output_file + '_autogen.cpp', json_file, namespace, enum_type)

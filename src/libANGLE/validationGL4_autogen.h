// GENERATED FILE - DO NOT EDIT.
// Generated by generate_entry_points.py using data from gl.xml and wgl.xml.
//
// Copyright 2019 The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//
// validationGL4_autogen.h:
//   Validation functions for the OpenGL 4.0 entry points.

#ifndef LIBANGLE_VALIDATION_GL4_AUTOGEN_H_
#define LIBANGLE_VALIDATION_GL4_AUTOGEN_H_

#include "common/PackedEnums.h"

namespace gl
{
class Context;

bool ValidateBeginQueryIndexed(Context *context, GLenum target, GLuint index, QueryID idPacked);
bool ValidateBlendEquationSeparatei(Context *context, GLuint buf, GLenum modeRGB, GLenum modeAlpha);
bool ValidateBlendEquationi(Context *context, GLuint buf, GLenum mode);
bool ValidateBlendFuncSeparatei(Context *context,
                                GLuint buf,
                                GLenum srcRGB,
                                GLenum dstRGB,
                                GLenum srcAlpha,
                                GLenum dstAlpha);
bool ValidateBlendFunci(Context *context, GLuint buf, GLenum src, GLenum dst);
bool ValidateDrawTransformFeedback(Context *context, GLenum mode, GLuint id);
bool ValidateDrawTransformFeedbackStream(Context *context, GLenum mode, GLuint id, GLuint stream);
bool ValidateEndQueryIndexed(Context *context, GLenum target, GLuint index);
bool ValidateGetActiveSubroutineName(Context *context,
                                     ShaderProgramID programPacked,
                                     GLenum shadertype,
                                     GLuint index,
                                     GLsizei bufsize,
                                     GLsizei *length,
                                     GLchar *name);
bool ValidateGetActiveSubroutineUniformName(Context *context,
                                            ShaderProgramID programPacked,
                                            GLenum shadertype,
                                            GLuint index,
                                            GLsizei bufsize,
                                            GLsizei *length,
                                            GLchar *name);
bool ValidateGetActiveSubroutineUniformiv(Context *context,
                                          ShaderProgramID programPacked,
                                          GLenum shadertype,
                                          GLuint index,
                                          GLenum pname,
                                          GLint *values);
bool ValidateGetProgramStageiv(Context *context,
                               ShaderProgramID programPacked,
                               GLenum shadertype,
                               GLenum pname,
                               GLint *values);
bool ValidateGetQueryIndexediv(Context *context,
                               GLenum target,
                               GLuint index,
                               GLenum pname,
                               GLint *params);
bool ValidateGetSubroutineIndex(Context *context,
                                ShaderProgramID programPacked,
                                GLenum shadertype,
                                const GLchar *name);
bool ValidateGetSubroutineUniformLocation(Context *context,
                                          ShaderProgramID programPacked,
                                          GLenum shadertype,
                                          const GLchar *name);
bool ValidateGetUniformSubroutineuiv(Context *context,
                                     GLenum shadertype,
                                     GLint location,
                                     GLuint *params);
bool ValidateGetUniformdv(Context *context,
                          ShaderProgramID programPacked,
                          GLint location,
                          GLdouble *params);
bool ValidateMinSampleShading(Context *context, GLfloat value);
bool ValidatePatchParameterfv(Context *context, GLenum pname, const GLfloat *values);
bool ValidatePatchParameteri(Context *context, GLenum pname, GLint value);
bool ValidateUniform1d(Context *context, GLint location, GLdouble x);
bool ValidateUniform1dv(Context *context, GLint location, GLsizei count, const GLdouble *value);
bool ValidateUniform2d(Context *context, GLint location, GLdouble x, GLdouble y);
bool ValidateUniform2dv(Context *context, GLint location, GLsizei count, const GLdouble *value);
bool ValidateUniform3d(Context *context, GLint location, GLdouble x, GLdouble y, GLdouble z);
bool ValidateUniform3dv(Context *context, GLint location, GLsizei count, const GLdouble *value);
bool ValidateUniform4d(Context *context,
                       GLint location,
                       GLdouble x,
                       GLdouble y,
                       GLdouble z,
                       GLdouble w);
bool ValidateUniform4dv(Context *context, GLint location, GLsizei count, const GLdouble *value);
bool ValidateUniformMatrix2dv(Context *context,
                              GLint location,
                              GLsizei count,
                              GLboolean transpose,
                              const GLdouble *value);
bool ValidateUniformMatrix2x3dv(Context *context,
                                GLint location,
                                GLsizei count,
                                GLboolean transpose,
                                const GLdouble *value);
bool ValidateUniformMatrix2x4dv(Context *context,
                                GLint location,
                                GLsizei count,
                                GLboolean transpose,
                                const GLdouble *value);
bool ValidateUniformMatrix3dv(Context *context,
                              GLint location,
                              GLsizei count,
                              GLboolean transpose,
                              const GLdouble *value);
bool ValidateUniformMatrix3x2dv(Context *context,
                                GLint location,
                                GLsizei count,
                                GLboolean transpose,
                                const GLdouble *value);
bool ValidateUniformMatrix3x4dv(Context *context,
                                GLint location,
                                GLsizei count,
                                GLboolean transpose,
                                const GLdouble *value);
bool ValidateUniformMatrix4dv(Context *context,
                              GLint location,
                              GLsizei count,
                              GLboolean transpose,
                              const GLdouble *value);
bool ValidateUniformMatrix4x2dv(Context *context,
                                GLint location,
                                GLsizei count,
                                GLboolean transpose,
                                const GLdouble *value);
bool ValidateUniformMatrix4x3dv(Context *context,
                                GLint location,
                                GLsizei count,
                                GLboolean transpose,
                                const GLdouble *value);
bool ValidateUniformSubroutinesuiv(Context *context,
                                   GLenum shadertype,
                                   GLsizei count,
                                   const GLuint *indices);
}  // namespace gl

#endif  // LIBANGLE_VALIDATION_GL4_AUTOGEN_H_

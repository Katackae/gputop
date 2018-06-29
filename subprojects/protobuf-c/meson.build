project('protobuf-c', 'c', 'cpp', version : '1.3.0', license : 'BSD-2')

c = meson.get_compiler('c')
cc = meson.get_compiler('cpp')

libprotobuf_c_src = [
  'protobuf-c/protobuf-c.c',
]

protobuf_c_flags = [ '-Wno-unused-parameter', '-Wno-sign-compare' ]

protobuf_dep = subproject('protobuf').get_variable('protobuf_dep')
libprotobuf_c = library('protobuf-c',
                        libprotobuf_c_src,
                        c_args: protobuf_c_flags,
                        dependencies: protobuf_dep,
                        include_directories: include_directories('protobuf-c'))
protobuf_c_dep = declare_dependency(link_with: libprotobuf_c,
                                    include_directories: include_directories('.'))

protoc_c_src = [
  'protoc-c/c_bytes_field.cc',
  'protoc-c/c_enum.cc',
  'protoc-c/c_enum_field.cc',
  'protoc-c/c_extension.cc',
  'protoc-c/c_field.cc',
  'protoc-c/c_file.cc',
  'protoc-c/c_generator.cc',
  'protoc-c/c_helpers.cc',
  'protoc-c/c_message.cc',
  'protoc-c/c_message_field.cc',
  'protoc-c/c_primitive_field.cc',
  'protoc-c/c_service.cc',
  'protoc-c/c_string_field.cc',
  'protoc-c/main.cc',
]

protoc_deps = subproject('protobuf').get_variable('protoc_dep')
protoc_c = executable('protoc-c',
                      protoc_c_src,
                      cpp_args: [protobuf_c_flags, '-DPACKAGE_STRING="protobuf-c"'],
                      include_directories: include_directories('protoc-c',
                                                               'protobuf-c'),
                      dependencies: protoc_deps)

protoc_native_deps = subproject('protobuf').get_variable('protoc_native_dep')
protoc_c_native = executable('protoc-c-native',
                             protoc_c_src,
                             cpp_args: [protobuf_c_flags, '-DPACKAGE_STRING="protobuf-c"'],
                             include_directories: include_directories('protoc-c',
                                                                      'protobuf-c'),
                             dependencies: protoc_native_deps,
                             native: true)

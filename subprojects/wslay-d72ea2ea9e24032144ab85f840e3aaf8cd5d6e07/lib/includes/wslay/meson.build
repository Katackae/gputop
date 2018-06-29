wslayver_h = custom_target(
  'wslayver.h',
  input : 'wslayver.h.in',
  output : 'wslayver.h',
  command : [ find_program('python'),
              join_paths(meson.current_source_dir(), 'gen_wslayver.py'),
              '--variable',
              'PACKAGE_VERSION=' + meson.project_version(),
              '--input', '@INPUT@',
              '--output', '@OUTPUT@', ])

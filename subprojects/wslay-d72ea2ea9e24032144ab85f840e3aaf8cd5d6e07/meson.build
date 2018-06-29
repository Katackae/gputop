project('wslay', 'c', version : '1.0.0', license : 'MIT')

wslay_flags = []

wslay_src = [
  'lib/wslay_event.c',
  'lib/wslay_frame.c',
  'lib/wslay_net.c',
  'lib/wslay_queue.c',
  'lib/wslay_stack.c',
]

wslay_hdr = files(
  'lib/wslay_event.h',
  'lib/wslay_frame.h',
  'lib/wslay_net.h',
  'lib/wslay_queue.h',
  'lib/wslay_stack.h'
)

subdir('lib/includes/wslay')

wslay_src += wslayver_h

wslay = library('wslay',
                wslay_src,
                c_args: wslay_flags,
                include_directories: include_directories('lib', 'lib/includes'))

wslay_dep = declare_dependency(link_with: wslay,
                               include_directories: include_directories('lib/includes'))

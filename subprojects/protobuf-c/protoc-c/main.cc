#include <string>

#include <google/protobuf/compiler/plugin.h>
#include <google/protobuf/compiler/command_line_interface.h>
#include <protoc-c/c_generator.h>

int main(int argc, char* argv[]) {
  google::protobuf::compiler::c::CGenerator c_generator;
  google::protobuf::compiler::CommandLineInterface cli;
  cli.RegisterGenerator("--c_out", &c_generator, "Generate C/H files.");
  cli.SetVersionInfo(PACKAGE_STRING);
  return cli.Run(argc, argv);
}

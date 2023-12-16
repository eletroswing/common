import sys
import os
import subprocess
import json

def update_file_imports(file_path, old_import, new_import):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            updated_line = line.replace(old_import, new_import)
            file.write(updated_line)

def remove_dependency_from_package_json(package_name, save_dev, script_directory):
    if(os.path.exists(package_json_path)):
        package_json_path = os.path.join(script_directory, 'package.json')

        with open(package_json_path, 'r') as package_json_file:
            package_data = json.load(package_json_file)

        dependencies_key = 'devDependencies' if save_dev else 'dependencies'

        if dependencies_key not in package_data:
            print(f"The dependencie '{package_name}' is not present on package.json.")
            return

        if package_name in package_data[dependencies_key]:
            del package_data[dependencies_key][package_name]

            with open(package_json_path, 'w') as package_json_file:
                json.dump(package_data, package_json_file, indent=2)

            print(f"Dependencie '{package_name}' removed package.json.")
        else:
            print(f"The dependencie '{package_name}' is not present on package.json.")


def add_dependency_to_package_json(package_name, save_dev, dir):
    package_json_path = os.path.join(dir, 'package.json')
    if(os.path.exists(package_json_path)):
        with open(package_json_path, 'r') as package_json_file:
            package_data = json.load(package_json_file)

        dependencies_key = 'devDependencies' if save_dev else 'dependencies'

        if dependencies_key not in package_data:
            package_data[dependencies_key] = {}

        if package_name not in package_data[dependencies_key]:
            package_data[dependencies_key][package_name] = "latest"  

            with open(package_json_path, 'w') as package_json_file:
                json.dump(package_data, package_json_file, indent=2)

            print(f"Dependencie '{package_name}' added.")
        else:
            print(f"The dependencie'{package_name}' already present")
    else:
        print('packge doest not exists', package_json_path)
def createDirectory(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as e:
            pass

arguments = sys.argv

script_directory = os.path.dirname(os.path.realpath(__file__))
current_working_directory = os.getcwd()

if(len(arguments) >= 2):
    if arguments[1] == 'npm':
        if arguments[2] == 'install':
            if(len(arguments) >= 4):
                package_name = arguments[3]
                save_dev = '--save-dev' in arguments

                subprocess.run('npm install {} --prefix {}/libs'.format(package_name, script_directory), shell=True, capture_output=True, text=True)
                add_dependency_to_package_json(package_name, save_dev, current_working_directory)

                common_directory = os.path.join(current_working_directory, 'node_modules')
                createDirectory(common_directory)

                js_content = """const {} = require('{}');

module.exports = {};
                """.format(package_name, script_directory.replace("\\", "/") + "/libs/node_modules/" + package_name, package_name)

                js_path = os.path.join(common_directory, "{}.js".format(package_name))
                with open(js_path, "w+") as archive:
                    archive.write(js_content)

            else:
                package_json_path = os.path.join(script_directory, 'libs', 'package.json')
                if(os.path.exists(package_json_path)):

                    subprocess.run('npm install --prefix {}/libs'.format(script_directory), shell=True, capture_output=True, text=True)

                    with open(package_json_path, 'r') as package_json_file:
                        package_data = json.load(package_json_file)

                    dependencies = package_data.get('dependencies', {}).items()
                    dev_dependencies = package_data.get('devDependencies', {}).items()

                    common_directory = os.path.join(current_working_directory, 'node_modules')
                    createDirectory(common_directory)

                    if bool(dependencies):
                        for package_name, version in dependencies:
                            js_content = """const {} = require('{}');

    module.exports = {};
                    """.format(package_name, script_directory.replace("\\", "/") + "/libs/node_modules/" + package_name, package_name)

                            js_path = os.path.join(common_directory, "{}.js".format(package_name))
                            with open(js_path, "w+") as archive:
                                archive.write(js_content)

                    if bool(dev_dependencies):
                        for package_name, version in dev_dependencies:
                            js_content = """const {} = require('{}');

module.exports = {};
                """.format(package_name, script_directory.replace("\\", "/") + "/libs/node_modules/" + package_name, package_name)

                        js_path = os.path.join(common_directory, "{}.js".format(package_name))
                        with open(js_path, "w+") as archive:
                            archive.write(js_content)


        elif arguments[2] == 'uninstall':
            if(arguments[3]):
                package_name = arguments[3]

                js_path = os.path.join(current_working_directory, 'node_modules', "{}.js".format(package_name))
                if os.path.exists(js_path):
                    os.remove(js_path)
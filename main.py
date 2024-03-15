import yaml
import os

breakpointLineBeginnings = []
filesToParse = []
gdbConfigFile = ""
breakpoints = []

#taken from: https://stackoverflow.com/a/1432949, sets cwd to location of this file.
# TODO: support custom directory locations via yaml file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#loads data from the yaml file to variables
with open("autoBreakConfig.yaml") as yamlFile:
	data = yaml.safe_load(yamlFile)
	filesToParse = data["files_to_parse"].copy() #[file for file in data["files_to_parse"]]
	gdbConfigFile = data["gdb_config_file"]
	breakpointLineBeginnings = data["breakpoint_line_beginning"]

for file in filesToParse:
	with open(file) as parsingFile:
		for lineNumber, line in enumerate(parsingFile):
			print(f"{lineNumber+1}: {str(line).strip()}")
			if str(line).lstrip().startswith(tuple(breakpointLineBeginnings)):
				print(f"We need to break on line {lineNumber+1}")
				breakpoints.append(f"break {file}:{lineNumber+1}")


if gdbConfigFile not in os.listdir():
	#TODO: Support creating a .gdbinit file
	print(f"{gdbConfigFile} not found in cwd: {os.getcwd()}")
	pass
else:
	with open(gdbConfigFile, 'r') as gdbinit:
		lines=gdbinit.readlines()
	try:
		print(lines)
		startSegment = lines.index("#start: breakpoints\n")
	except ValueError:
		#TODO: add proper handling
		print("did not find start")
		startSegment = 1
		breakpoints.insert(0, "#start: breakpoints")
		breakpoints.append("#end: breakpoints")
		
	finally:
		for index,breakpoint in enumerate(breakpoints):
			lines.insert(startSegment+index+1, f"{breakpoint}\n")
		with open(gdbConfigFile, 'w') as gdbinit:
			gdbinit.writelines(lines) 
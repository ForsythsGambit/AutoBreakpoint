# AutoBreakpoint
Are you annoyed by code edits changing your frequently used breakpoints? Do you wish there was a way to tie your breakpoints to a comment in your code instead of an ehtereal line number? Well now there is!


Just specify your source files, how you want breakpoint-comments to start, and your GDB config file if it's not `.gdbinit` all in `autoBreakConfig.yaml`!


`test.c` is included and `autoBreakConfig.yaml` is preconfigured as an example. Simply run `python3 main.py` and `.gdbinit` will be edited to add breakpoints as specified in `test.c`.

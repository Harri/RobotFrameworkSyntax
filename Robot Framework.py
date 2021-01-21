import sublime
import sublime_plugin
import subprocess


class robot_tidy(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings('Robot Framework.sublime-settings')
        python_path = s.get('python_path')
        line_endings = self.view.line_endings()

        # ST supports CR line endings in addition to the line endings
        # Tidy supports (CRLF and LF). Need to not mess those files up.
        if line_endings.lower() not in ['windows', 'unix']:
            raise ValueError(
                'Current file line endings were set to "{}".'
                'Unfortunately Robot Framework Tidy only supports'
                '"native", "windows", and "unix".'.format(line_endings)
            )

        cmd = [python_path, '-m', 'robot.tidy', '--lineseparator',
               line_endings.lower(), self.view.file_name()]

        tidy_content = subprocess.check_output(
            cmd,
            shell=True,
            universal_newlines=True
        )

        region = sublime.Region(0, self.view.size())
        # If current buffer is different from buffer formatted by tidy,
        # replace the current buffer with tidy content
        if self.view.substr(region) != tidy_content:
            self.view.replace(edit, region, tidy_content)

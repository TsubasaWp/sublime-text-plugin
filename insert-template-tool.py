import sublime,sublime_plugin


class BluiCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        current = 0
        if len(self.view.sel()) > 0:
            current, _ = self.view.rowcol(self.view.sel()[0].a)
            current += 1
        point = self.view.text_point(current,0)
        self.view.insert(edit, point, "Hello, World!<#replace#>\n")
        self.view.sel().clear()
        rg = self.view.find("#replace#",point)
        self.view.sel().add(rg)
        self.view.replace(edit,rg,'')


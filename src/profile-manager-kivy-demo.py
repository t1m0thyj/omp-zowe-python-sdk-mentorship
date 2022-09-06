from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from zowe.core_for_zowe_sdk.profile_manager import ProfileManager
from zowe.zos_files_for_zowe_sdk import Files
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton

NAME_PATTERN: str = "MENTEE2*"


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(MyTreeLayout())
        self.label = Label(text="(Preview appears here)")
        self.add_widget(self.label)


class TreeViewButton(TreeViewNode, MDRectangleFlatIconButton):
    pass


class MyTreeLayout(TreeView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        prof = ProfileManager(appname="zowe")
        s = prof.load(profile_name="zosmf")
        self.files = Files(s)
        d = self.files.list_dsn(name_pattern=NAME_PATTERN)

        for items in d["items"]:
            try:
                naam = items["dsname"]
                res = self.files.list_dsn_members(dataset_name=items["dsname"])
                parent = self.add_node(TreeViewLabel(text=items["dsname"]))
                print("-----------------------------")
                print(res)
                print("-----------------------------")
                if len(res) == 0:
                    self.add_node(TreeViewButton(text="(empty)"), parent=parent)
                for members in res:
                    mem = members["member"]
                    self.add_node(
                        TreeViewButton(
                            text=f"{naam}({mem}).jcl",
                            on_press=self.print_stuff,
                            icon="script-text",
                        ),
                        parent=parent,
                    )
                    # self.add_node(TreeViewButton(text=members["member"]), parent=parent)
            except Exception as exc:
                self.add_node(
                    TreeViewButton(
                        text=items["dsname"],
                        on_press=self.print_stuff,
                        icon="script-text",
                    )
                )
                print("*****************************")
                print(exc)
                print("*****************************")

    def print_stuff(self, instance: TreeViewButton):
        content = self.files.get_dsn_content(dataset_name=instance.text)
        print("-----------------------------")
        print(content)
        print("-----------------------------")
        self.parent.label.text = content["response"]


class ZoweDatasetsViewerApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return MyGridLayout(cols=2)


if __name__ == "__main__":
    ZoweDatasetsViewerApp().run()

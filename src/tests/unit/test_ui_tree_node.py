from ui_tree.node import Bounds, Node


def test_add_child_and_parent_links() -> None:
    """Проверяет, что add_child устанавливает ссылки parent/children корректно."""

    root = Node(id="root", type="screen")
    child = Node(id="child", type="button")

    root.add_child(child)

    assert child.parent is root
    assert child in root.children


def test_find_first_by_predicate() -> None:
    """Проверяет поиск первого узла по предикату."""

    root = Node(id="root", type="screen")
    ok_button = Node(id="ok", type="button", text="OK")
    cancel_button = Node(id="cancel", type="button", text="Cancel")
    root.add_child(ok_button)
    root.add_child(cancel_button)

    found = root.find_first(lambda n: n.text == "Cancel")

    assert found is cancel_button


def test_find_all_with_broken_nodes() -> None:
    """Проверяет, что find_all возвращает все подходящие узлы, включая узлы без bounds."""

    root = Node(id="root", type="screen")
    good = Node(id="good", type="label", bounds=Bounds(x=0, y=0, width=10, height=10))
    broken = Node(id="broken", type="label", bounds=None)
    root.add_child(good)
    root.add_child(broken)

    found = root.find_all(lambda n: n.type == "label")

    assert len(found) == 2

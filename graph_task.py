from collections import defaultdict
import unittest


def build_dfs_tree(graph):
    """
    Строит глубинное остовное дерево (DFS) для неориентированного графа.

    Аргументы:
        graph (list of list): Список смежности графа, где graph[i]
        содержит соседей вершины i.

    Возвращает:
        dict: Словарь, где ключи - вершины, значения -
        списки дочерних вершин в дереве.
    """
    n = len(graph)
    visited = set()
    tree = defaultdict(list)

    # Выбираем начальную вершину (0 по умолчанию)
    start = 0
    visited.add(start)

    def dfs(u, parent):
        """Рекурсивная функция для обхода графа в глубину."""
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                tree[u].append(v)
                dfs(v, u)

    dfs(start, -1)  # Начальная вершина не имеет родителя
    # Преобразуем defaultdict в обычный dict для предсказуемости в тестах
    return {u: sorted(children) for u, children in tree.items()}


# Примеры запуска программы
if __name__ == "__main__":
    # Пример 1: Граф с циклом
    graph_cycle = [
        [1, 2],     # 0
        [0, 2],     # 1
        [0, 1, 3],  # 2
        [2]         # 3
    ]
    dfs_tree = build_dfs_tree(graph_cycle)
    print("Пример 1: Остовное дерево для графа с циклом")
    for node in sorted(dfs_tree):
        print(f"{node} -> {dfs_tree[node]}")

    # Пример 2: Линейный граф 0-1-2-3
    graph_linear = [
        [1],     # 0
        [0, 2],  # 1
        [1, 3],  # 2
        [2]      # 3
    ]
    dfs_tree_linear = build_dfs_tree(graph_linear)
    print("\nПример 2: Остовное дерево для линейного графа")
    for node in sorted(dfs_tree_linear):
        print(f"{node} -> {dfs_tree_linear[node]}")


# Модульные тесты
class TestDFSTree(unittest.TestCase):
    def test_empty_graph(self):
        """Тест для пустого графа (одна вершина без рёбер)."""
        graph = [[]]
        expected = {}
        self.assertEqual(build_dfs_tree(graph), expected)

    def test_single_node(self):
        """Тест для графа из одной вершины."""
        graph = [[]]
        expected = {}
        self.assertEqual(build_dfs_tree(graph), expected)

    def test_linear_graph(self):
        """Тест для линейного графа 0-1-2-3."""
        graph = [[1], [0, 2], [1, 3], [2]]
        expected = {
            0: [1],
            1: [2],
            2: [3]
        }
        self.assertEqual(build_dfs_tree(graph), expected)

    def test_cyclic_graph(self):
        """Тест для циклического графа."""
        graph = [
            [1, 2],
            [0, 2],
            [0, 1, 3],
            [2]
        ]
        expected = {
            0: [1],
            1: [2],
            2: [3]
        }
        self.assertEqual(build_dfs_tree(graph), expected)

    def test_binary_tree_structure(self):
        """Тест для графа в виде двоичного дерева."""
        graph = [
            [1, 2],     # 0
            [0, 3, 4],  # 1
            [0, 5, 6],  # 2
            [1],        # 3
            [1],        # 4
            [2],        # 5
            [2]         # 6
        ]
        result = build_dfs_tree(graph)
        # Проверяем структуру дерева
        self.assertEqual(result[0], [1, 2])
        self.assertEqual(result[1], [3, 4])
        self.assertEqual(result[2], [5, 6])
        self.assertNotIn(3, result)
        self.assertNotIn(4, result)
        self.assertNotIn(5, result)
        self.assertNotIn(6, result)


# Запуск тестов при выполнении скрипта
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

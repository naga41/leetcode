import main
import unittest


class Test(unittest.TestCase):

    def test_init(self):
        obj = main.MyLinkedList()
        self.assertEqual(0, obj.size)

    def test_get(self):
        obj = main.MyLinkedList()
        # invalid index
        self.assertEqual(-1, obj.get(-1))
        self.assertEqual(-1, obj.get(1))

        obj.addAtIndex(0, 10)
        self.assertEqual(10, obj.get(0))

        obj.addAtHead(0)
        self.assertEqual(10, obj.get(1))
        self.assertEqual(0, obj.get(0))

        obj.addAtTail(1)
        self.assertEqual(10, obj.get(1))
        self.assertEqual(1, obj.get(2))

        obj.addAtIndex(3, 10)
        self.assertEqual(10, obj.get(3))

        obj.deleteAtIndex(3)
        self.assertEqual(3, obj.size)
        self.assertEqual(0, obj.get(0))
        self.assertEqual(1, obj.get(2))


if __name__ == "__main__":
    unittest.main()

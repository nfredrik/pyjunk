import unittest

class TestDefectModel(unittest.TestCase):
    def test_getDefectList(self):
        # defect_model = DefectModel()
        # self.assertEqual(expected, defect_model.getDefectList(component))
        assert False # TODO: implement your test here

    def test_getSummary(self):
        # defect_model = DefectModel()
        # self.assertEqual(expected, defect_model.getSummary(id))
        assert False # TODO: implement your test here

class TestDefectView(unittest.TestCase):
    def test_defectList(self):
        # defect_view = DefectView()
        # self.assertEqual(expected, defect_view.defectList(list, category))
        assert False # TODO: implement your test here

    def test_summary(self):
        # defect_view = DefectView()
        # self.assertEqual(expected, defect_view.summary(summary, defectid))
        assert False # TODO: implement your test here

class TestFileDefectView(unittest.TestCase):
    def test___del__(self):
        # file_defect_view = FileDefectView(filename)
        # self.assertEqual(expected, file_defect_view.__del__())
        assert False # TODO: implement your test here

    def test___init__(self):
        # file_defect_view = FileDefectView(filename)
        assert False # TODO: implement your test here

    def test_defectList(self):
        # file_defect_view = FileDefectView(filename)
        # self.assertEqual(expected, file_defect_view.defectList(list, category))
        assert False # TODO: implement your test here

    def test_summary(self):
        # file_defect_view = FileDefectView(filename)
        # self.assertEqual(expected, file_defect_view.summary(summary, defectid))
        assert False # TODO: implement your test here

class TestController(unittest.TestCase):
    def test___init__(self):
        # controller = Controller(model, view)
        assert False # TODO: implement your test here

    def test_getDefectList(self):
        # controller = Controller(model, view)
        # self.assertEqual(expected, controller.getDefectList(component))
        assert False # TODO: implement your test here

    def test_getDefectSummary(self):
        # controller = Controller(model, view)
        # self.assertEqual(expected, controller.getDefectSummary(defectid))
        assert False # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()

import importlib.util
import json
import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('demo_tools', root / 'productivity_agent/tools.py')
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)

class ToolTests(unittest.TestCase):
    def test_reads_and_writes(self):
        with TemporaryDirectory() as folder:
            original = root / 'productivity_agent/sample_data.json'
            tools.DATA = Path(folder) / 'data.json'
            self.assertFalse(tools.DATA.exists())
            self.assertEqual(len(tools.get_tasks()['tasks']), 3)
            self.assertTrue(tools.DATA.exists())
            self.assertEqual(original.read_text(), tools.SAMPLE.read_text())
            self.assertEqual(len(tools.get_schedule()['schedule']), 2)
            self.assertEqual(tools.add_task('Test robot battery','2026-11-29','high')['status'],'success')
            self.assertEqual(len(tools.get_tasks()['tasks']), 4)
            self.assertEqual(tools.add_task('Test robot battery','2026-11-29','high')['status'],'error')
            self.assertEqual(tools.add_task('bad','tomorrow','high')['status'],'error')
            self.assertEqual(tools.add_task('bad','2026-11-29','urgent')['status'],'error')

if __name__ == '__main__':
    unittest.main()

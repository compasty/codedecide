import os
import unittest

from codedecide import IndicatorPlotConfig


class TestIndicators(unittest.TestCase):
    def test_config(self):
        config1 = IndicatorPlotConfig(col_name='r1', trace_name='r1')
        self.assertEqual(config1.col_name, 'r1')
        self.assertIsNone(config1.legend_group)
        self.assertTrue(config1.separate)
        config2 = IndicatorPlotConfig(
            col_name='r2', trace_name='r2', separate=False)
        self.assertEqual(config2.col_name, 'r2')
        self.assertFalse(config2.separate)

    def test_os_env(self) -> None:
        self.assertIsNone(os.environ['NOT_EXIST'])

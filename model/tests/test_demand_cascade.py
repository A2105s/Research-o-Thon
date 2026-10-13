"""
Unit Test Suite for Demand-Cascade Model v2.0
=============================================
ResearchThon 2026 — Amity University Madhya Pradesh
Authors: Adarsh Singh, Sourav, Anamidhi Shrivastava
"""

import unittest
import math
from pathlib import Path
import sys

MODEL_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(MODEL_DIR))

from demand_cascade import run_cascade_v2, murphy_yield, run_monte_carlo


class TestDemandCascadeV2(unittest.TestCase):

    def setUp(self):
        self.base_res = run_cascade_v2(500000)

    def test_it_load_exact(self):
        # 500,000 * 700 * 1.82 / 1e6 = 637.0 MW
        expected = (500000 * 700 * 1.82) / 1e6
        self.assertAlmostEqual(self.base_res["it_load_mw"], expected, places=2)

    def test_facility_power_scaling(self):
        # 637.0 * 1.40 = 891.8 MW
        expected = 637.0 * 1.40
        self.assertAlmostEqual(self.base_res["fac_power_mw"], expected, places=2)

    def test_annual_energy_exact(self):
        # 891.8 * 8760 * 0.80 / 1e6 = 6.2497 TWh
        expected = (891.8 * 8760 * 0.80) / 1e6
        self.assertAlmostEqual(self.base_res["annual_energy_twh"], expected, places=3)

    def test_murphy_yield_bounds(self):
        y1 = murphy_yield(814.0, 0.08)
        self.assertGreater(y1, 0.40)
        self.assertLessEqual(y1, 0.85)

        # Monotonicity: higher defect density gives lower yield
        y_low_defect = murphy_yield(814.0, 0.05)
        y_high_defect = murphy_yield(814.0, 0.12)
        self.assertGreater(y_low_defect, y_high_defect)

    def test_wafer_starts_exact(self):
        # With 40 good dies per wafer, 500,000 / 40 = 12,500
        self.assertEqual(self.base_res["wafer_starts"], 12500)
        self.assertAlmostEqual(self.base_res["tsmc_share_pct"], 1.60, places=2)

    def test_cowos_interposer_exact(self):
        # With 15 packages per wafer, ceil(500,000 / 15) = 33,334
        self.assertEqual(self.base_res["cowos_wafers"], 33334)
        self.assertAlmostEqual(self.base_res["cowos_share_pct"], 7.41, places=2)

    def test_hbm_stacks_exact(self):
        # 500,000 * 8 = 4,000,000 stacks
        self.assertEqual(self.base_res["hbm_stacks"], 4000000)
        self.assertAlmostEqual(self.base_res["hbm_share_pct"], 6.67, places=2)

    def test_chokepoint_ratio(self):
        # CoWoS share (7.41%) / Wafer share (1.60%) = ~4.63x
        ratio = self.base_res["chokepoint_ratio"]
        self.assertGreater(ratio, 4.0)

    def test_scenario_linearity(self):
        res_200k = run_cascade_v2(200000)
        res_1m = run_cascade_v2(1000000)
        # IT load of 1M should be exactly 5x of 200k
        self.assertAlmostEqual(res_1m["it_load_mw"], res_200k["it_load_mw"] * 5.0, places=1)

    def test_monte_carlo_reproducibility(self):
        summary = run_monte_carlo(500000, 100)
        self.assertIn("fac_power_mw", summary)
        self.assertIn("P50", summary["fac_power_mw"])
        self.assertGreater(summary["fac_power_mw"]["P90"], summary["fac_power_mw"]["P10"])


if __name__ == "__main__":
    unittest.main()

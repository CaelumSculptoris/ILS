import unittest

from ils_simulator.model import build_field, lexical_baseline, run_experiment


class SimulatorTests(unittest.TestCase):
    def test_field_has_explicit_held_out_frontier(self):
        frontier = [c for c in build_field().concepts.values() if c.frontier]
        self.assertGreaterEqual(len(frontier), 3)

    def test_metrics_are_bounded(self):
        result = run_experiment(seed=3)
        for metrics in (result.ensemble, result.lexical):
            self.assertGreaterEqual(metrics.precision, 0.0)
            self.assertLessEqual(metrics.precision, 1.0)
            self.assertGreaterEqual(metrics.recall, 0.0)
            self.assertLessEqual(metrics.recall, 1.0)

    def test_same_seed_is_reproducible(self):
        self.assertEqual(run_experiment(11), run_experiment(11))

    def test_ensemble_can_recover_frontier_in_synthetic_world(self):
        result = run_experiment(seed=7)
        self.assertGreater(result.ensemble.recall, 0.0)
        self.assertGreaterEqual(result.ensemble.recall, result.lexical.recall)

    def test_lexical_baseline_does_not_know_hidden_frontier_terms(self):
        field = build_field()
        metrics = lexical_baseline(field, [])
        self.assertEqual(metrics.recall, 0.0)


if __name__ == "__main__":
    unittest.main()

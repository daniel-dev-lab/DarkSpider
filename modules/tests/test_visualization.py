import os
import shutil
import unittest

from modules.checker import extract_domain, folder
from modules.crawler import Crawler
from modules.helpers.helper import Capturing
from modules.visualization import Visualization


def test_plots(self, _func):
    """Base test function for all the plots."""
    with Capturing() as result:
        _func()

    expected = [f"## {_func.__doc__}..."]
    self.assertEqual(
        expected,
        result,
        f"Test Fail:: {_func.__name__} returned = {result}, expected {expected}",
    )

    output = os.path.join(self.obj.out_path, f"{_func.__name__}.png")
    self.assertTrue(
        os.path.exists(output),
        f"Test Fail:: File: {output} - does not exist",
    )


class TestVisualizationFunctions(unittest.TestCase):
    """Unit test for Visualization module."""

    def setUp(self):
        self._website = "http://info.cern.ch/"
        self.out_path = out_path = folder(extract_domain(self._website), False)

        self.crawler = Crawler(
            website=self._website,
            c_depth=2,
            c_pause=1,
            out_path=out_path,
            external=True,
            logs=False,
            verbose=False,
            exclusion=None,
        )

        with Capturing() as _:
            self.crawler.crawl()

        self.obj = Visualization(
            json_file=out_path + "/network_structure.json",
            out_path=out_path,
            verbose=True,
        )

    def tearDown(self):
        """Test Suite Teardown."""
        # Remove test folder.
        shutil.rmtree(self.out_path)

    def test_indegree_plot(self):
        """Test visualization.indegree_plot function.
        Scatter Plot of the indegree vs nodes of the graph.
        """
        test_plots(self, self.obj.indegree_plot)

    def test_indegree_bar(self):
        """Test visualization.indegree_bar function.
        Bar Graph of the indegree vs percentage of nodes of the graph.
        """
        test_plots(self, self.obj.indegree_bar)

    def test_outdegree_plot(self):
        """Test visualization.outdegree_plot function.
        Scatter Plot of the outdegree vs nodes of the graph.
        """
        test_plots(self, self.obj.outdegree_plot)

    def test_outdegree_bar(self):
        """Test visualization.outdegree_bar function.
        Bar Graph of the outdegree vs percentage of nodes of the graph.
        """
        test_plots(self, self.obj.outdegree_bar)

    def test_eigenvector_centrality_bar(self):
        """Test visualization.eigenvector_centrality_bar function.
        Bar Graph of the eigenvector centrality vs percentage of nodes of the graph.
        """
        test_plots(self, self.obj.eigenvector_centrality_bar)

    def test_pagerank_bar(self):
        """Test visualization.pagerank_bar function.
        Bar Graph of the pagerank vs percentage of nodes of the graph.
        """
        test_plots(self, self.obj.pagerank_bar)

    def test_visualize(self):
        """Test visualization.visualize function.
        Visualization of the graph.
        """
        test_plots(self, self.obj.visualize)
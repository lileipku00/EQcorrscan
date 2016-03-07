"""
Functions to test generating templates from SAC data.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import unittest


class TestSACTemplateGeneration(unittest.TestCase):
    """Test the reading a writing of pick info."""
    def test_template_gen(self):
        """Test template generation."""
        from eqcorrscan.core.template_gen import from_sac
        import glob
        import os

        samp_rate = 20
        length = 8
        test_files = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                  'test_data', 'SAC', '*')
        sac_files = glob.glob(test_files)
        template = from_sac(sac_files, lowcut=2.0, highcut=8.0,
                            samp_rate=samp_rate, filt_order=4, length=length,
                            swin='all', prepick=0.1, debug=0, plot=False)
        for tr in template:
            self.assertEqual(len(tr.data), length * samp_rate)

if __name__ == '__main__':
    unittest.main()

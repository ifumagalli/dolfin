"""Unit tests for the XML io library for vectors"""

# Copyright (C) 2011 Garth N. Wells
#
# This file is part of DOLFIN.
#
# DOLFIN is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DOLFIN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with DOLFIN. If not, see <http://www.gnu.org/licenses/>.
#
# First added:  2011-06-17
# Last changed:

import unittest
from dolfin import *

class XML_vector_io(unittest.TestCase):
    """Test output of Meshes to XML files"""

    def test_save_vector(self):
        if has_linear_algebra_backend("PETSc"):
            # Create vector and write file
            x = PETScVector(197)
            x[:] = 1.0
            f = File("x.xml")
            f << x

        if has_linear_algebra_backend("Epetra"):
            # Create vector and write file
            x = EpetraVector(197)
            x[:] = 1.0
            f = File("x.xml")
            f << x

    def test_save_gzipped_vector(self):
        if has_linear_algebra_backend("PETSc"):
            # Create vector and write file
            x = PETScVector(197)
            x[:] = 1.0
            f = File("x.xml.gz")
            f << x


    def test_read_vector(self):
        if has_linear_algebra_backend("PETSc"):
            # Create vector and write file
            x = PETScVector(197)
            x[:] = 1.0
            f = File("x.xml")
            f << x

            # Read vector from previous write
            y = PETScVector()
            f >> y
            self.assertEqual(x.size(), y.size())
            self.assertAlmostEqual(x.norm("l2"), y.norm("l2"))


        if has_linear_algebra_backend("Epetra"):
            # Create vector and write file
            x = EpetraVector(197)
            x[:] = 1.0
            f = File("x.xml")
            f << x

            # Read vector from write
            y = EpetraVector()
            f >> y
            self.assertEqual(x.size(), y.size())
            self.assertAlmostEqual(x.norm("l2"), y.norm("l2"))

    def test_read_gzipped_vector(self):
        if has_linear_algebra_backend("PETSc"):
            # Create vector and write file
            x = PETScVector(197)
            x[:] = 1.0
            f = File("x.xml")
            f << x

            # Read vector from previous write
            y = PETScVector()
            f >> y
            self.assertEqual(x.size(), y.size())
            self.assertAlmostEqual(x.norm("l2"), y.norm("l2"))

    def test_save_read_vector(self):
        size = 512
        x = Vector(size)
        x[:] = 1.0

        out_file = File("test_vector_xml.xml")
        out_file << x

        y = Vector()
        out_file >> y
        self.assertEqual(x.size(), y.size())
        self.assertAlmostEqual((x - y).norm("l2"), 0.0)

if __name__ == "__main__":
    unittest.main()

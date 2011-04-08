// Copyright (C) 2010 Garth N. Wells.
// Licensed under the GNU LGPL Version 2.1.
//
// Modified by Anders Logg, 2010-2011.
//
// First added:  2010-02-10
// Last changed: 2011-04-07

#include <dolfin/mesh/Mesh.h>
#include <dolfin/mesh/MeshEntity.h>
#include <dolfin/mesh/MeshFunction.h>
#include "UniformMeshRefinement.h"
#include "LocalMeshRefinement.h"
#include "refine.h"

using namespace dolfin;

//-----------------------------------------------------------------------------
dolfin::Mesh dolfin::refine(const Mesh& mesh)
{
  Mesh refined_mesh;
  UniformMeshRefinement::refine(refined_mesh, mesh);
  return refined_mesh;
}
//-----------------------------------------------------------------------------
void dolfin::refine(Mesh& refined_mesh, const Mesh& mesh)
{
  UniformMeshRefinement::refine(refined_mesh, mesh);
}
//-----------------------------------------------------------------------------
dolfin::Mesh dolfin::refine(const Mesh& mesh,
                            const MeshFunction<bool>& cell_markers)
{
  Mesh refined_mesh;
  refine(refined_mesh, mesh, cell_markers);
  return refined_mesh;
}
//-----------------------------------------------------------------------------
void dolfin::refine(Mesh& refined_mesh,
                    const Mesh& mesh,
                    const MeshFunction<bool>& cell_markers)
{
  // Call local mesh refinement algorithm
  LocalMeshRefinement::refine(refined_mesh, mesh, cell_markers);
}
//-----------------------------------------------------------------------------
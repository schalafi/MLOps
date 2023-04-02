def dot(u,v):
    assert len(u) == len(v),f"Vectors must have the same length, got for u {len(u)} and {len(v)}"

    return sum(u[i]*v[i] for i in range(len(u)))
    
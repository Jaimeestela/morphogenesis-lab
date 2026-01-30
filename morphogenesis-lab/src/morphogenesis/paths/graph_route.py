"""
Graph-based routing: connect rooms via corridors to a collector.
Uses networkx for shortest path when graph is provided.
"""

from __future__ import annotations

from typing import List, Tuple, Dict, Optional
import networkx as nx
from shapely.geometry import Polygon, Point, LineString


def build_room_graph(
    rooms: Dict[str, Polygon],
    adjacency: Dict[str, List[str]],
) -> nx.Graph:
    """
    Build graph with rooms as nodes. Edges from adjacency; weight = distance between centroids.
    """
    G = nx.Graph()
    for rid, poly in rooms.items():
        G.add_node(rid, centroid=(poly.centroid.x, poly.centroid.y))
    for rid, neighbors in adjacency.items():
        c0 = G.nodes[rid]["centroid"]
        for nid in neighbors:
            if nid in G and rid < nid:
                c1 = G.nodes[nid]["centroid"]
                d = ((c0[0] - c1[0]) ** 2 + (c0[1] - c1[1]) ** 2) ** 0.5
                G.add_edge(rid, nid, weight=d)
    return G


def route_to_collector(
    room_id: str,
    collector_node: str,
    G: nx.Graph,
) -> List[str]:
    """Shortest path (node list) from room_id to collector_node."""
    try:
        return nx.shortest_path(G, room_id, collector_node, weight="weight")
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return []


def path_geometry(
    node_ids: List[str],
    G: nx.Graph,
) -> List[Tuple[float, float]]:
    """Polyline from list of node ids (centroids)."""
    return [G.nodes[nid]["centroid"] for nid in node_ids]

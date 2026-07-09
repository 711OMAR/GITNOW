# Frontend — Auto Memories Doll

Production stack: **Next.js 14 · React 18 · TypeScript · TailwindCSS · Framer
Motion · React Flow (graph) · Leaflet (map) · ECharts (analytics)**.

## The design prototype
`../auto-memories-doll-dashboard.html` (repo root) is a **fully interactive,
self-contained prototype** of the entire dashboard — every view, the force
graph, charts, and map — rendering the final Violet Evergarden aesthetic. Use it
as the visual source of truth when porting components into the Next.js app.

Suggested component map:
- `app/(dashboard)/page.tsx`  → Overview
- `components/graph/RelationshipGraph.tsx` → React Flow port of the SVG graph
- `components/map/AtlasMap.tsx` → react-leaflet + markercluster
- `components/charts/*` → echarts-for-react panels
- `lib/api.ts` → typed client for the FastAPI endpoints
- `lib/theme.ts` → the design tokens (colors/fonts) from the prototype

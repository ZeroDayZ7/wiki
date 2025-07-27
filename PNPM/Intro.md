pnpm outdated
pnpm update
pnpm update --latest

pnpm list @neo/ui --filter web


To jawnie mówi: „dodaj tę paczkę jako local workspace package”, a nie ściągaj z NPM.
pnpm add @neo/ui@workspace:* --filter web

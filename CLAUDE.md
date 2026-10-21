# Content machine (cloud)

This repo holds the creator's short-form content machine: they help health systems turn messy data into reliable
reporting on Microsoft Fabric. What they sell is in `content-machine/fabric-field-guide.md`.

- Skills: `.claude/skills/content-machine` (the 5 systems) and `.claude/skills/nextphase-persa-shorts` (the editor, with
  the creator's brand in `brand/`). The SessionStart hook links them to `~/.claude/skills/`, links the workspace
  `content-machine/` to `~/content-machine/`, and gets the editor's tools ready, so the paths in the skills work as written.
- Sessions run in temporary containers. After a system writes to `~/content-machine/` (profile, voice, ideas, scripts,
  NOTES.md, covers) or changes the brand, commit and push it, or it is lost when the session ends.
- Video and audio files are git-ignored. Send every finished edit and render to the creator as a file in the session.
- Nothing is published, posted, scheduled or uploaded without the creator's explicit OK for that exact item.

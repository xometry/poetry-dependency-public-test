# Dependency/dependabot checking

This is a test repository for github support. This project uses poetry python package management. The github dependency graph is not working, but dependabot can work with an explicit config file, but the behavior is strange.

## Github settings

* Settings > Security & analysis > Dependency graph - Enabled (always on for public repos)
* Settings > Security & analysis > Dependabot alerts - Enabled
* Settings > Security & analysis > Dependabot security updates - Disabled
* `.github/dependabot.yml` is checked in and configured with "pip"-style dependencies

## Unexpected behavior

* Insights > Dependency graph says "No manifest files found: To enable the dependency graph, your repository must define dependencies in one of the supported manifest file types, like package.json or Gemfile."
* Security > Overview > Dependabot alerts has an "Enable Dependabot alerts" button, even though the settings pane already has alerts enabled?
* Security > Dependabot alerts: no alerts shown
* PRs: PR #1 *was* opened by dependabot to upgrade httplib2, even though dependabot security updates were explicitly disabled!
  
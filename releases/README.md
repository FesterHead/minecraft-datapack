# Releases

This directory is used to store built releases of the Minecraft datapack.

## Purpose

When a new version of the datapack is ready for distribution, it is built/packaged into a `.zip` archive and placed in this folder.

To prevent binary bloat in the git repository, all `.zip` files in this directory are ignored by Git.

## Installation

To use a built release in your Minecraft world:

1. Locate the built `.zip` file for the version you want to install.
2. Copy the `.zip` file.
3. Open your Minecraft saves folder:
   - **Windows**: `%appdata%\.minecraft\saves\`
   - **macOS**: `~/Library/Application Support/minecraft/saves/`
   - **Linux**: `~/.minecraft/saves/`
4. Select the world you want to add the datapack to.
5. Open the `datapacks` folder inside the world directory.
6. Paste the `.zip` file there.
7. Start Minecraft, load the world, and run the `/reload` command if the world was already open.

import os
import shutil
import zipfile
from pathlib import Path

def main():
    try:
        # Determine script root directory
        script_root = Path(__file__).parent.resolve()
        
        # Path to versioning.properties
        version_file = script_root / "versioning.properties"
        if not version_file.exists():
            print(f"Error: {version_file.name} not found!")
            return 1
            
        # Parse versioning.properties
        props = {}
        with open(version_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    props[key.strip()] = val.strip()
                    
        base_name = props.get("base")
        mc_version = props.get("minecraft-version")
        pack_version = props.get("datapack-version")
        
        if not (base_name and mc_version and pack_version):
            print("Error: Missing required keys in versioning.properties (base, minecraft-version, datapack-version)")
            return 1
            
        # Ensure releases directory exists
        releases_dir = script_root / "releases"
        releases_dir.mkdir(parents=True, exist_ok=True)
        
        # Define output zip path
        output_filename = f"{base_name}-{mc_version}-v{pack_version}.zip"
        output_path = releases_dir / output_filename
        
        # Remove existing zip if present
        if output_path.exists():
            output_path.unlink()
            print(f"Removed existing {output_filename}")
            
        # Ensure source directory exists
        source_dir = script_root / "data-pack-files"
        if not source_dir.exists():
            print(f"Error: {source_dir.name} directory not found!")
            return 1
            
        print(f"Creating {output_filename} in releases folder...")
        
        # Build the zip file
        docs_to_include = ["CHANGELOG.md", "LICENSE", "README.md"]
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            # 1. Add contents of data-pack-files to the root of the archive
            for file_path in source_dir.rglob("*"):
                if file_path.is_file():
                    # Compute path relative to source_dir so files are at root of zip
                    arcname = file_path.relative_to(source_dir)
                    # Skip files that will be overwritten by the repository docs at the root
                    if arcname.as_posix() in docs_to_include:
                        continue
                    zip_file.write(file_path, arcname=arcname)
                    
            # 2. Add documentation files to the root of the archive
            for doc in docs_to_include:
                doc_path = script_root / doc
                if doc_path.exists() and doc_path.is_file():
                    zip_file.write(doc_path, arcname=doc)
                else:
                    print(f"Warning: {doc} not found, skipping.")
                    
        # Print file size in KB
        size_kb = round(output_path.stat().st_size / 1024, 2)
        print(f"Successfully created releases\\{output_filename}")
        print(f"Size: {size_kb} KB")
        return 0
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())

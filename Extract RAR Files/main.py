import aspose.zip as az

with az.rar.RarArchive("archive.rar") as archive:
  
    archive.extract_to_directory("extracted_rar")

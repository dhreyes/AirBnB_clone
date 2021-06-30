#!/usr/bin/env python3
"""
Initializer for uniq instance of FileStorage
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

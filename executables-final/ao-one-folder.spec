# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\src\\frontend.py'],
             pathex=['.', '..\\src'],
             binaries=[],
             datas=[('..\\src\\frontend.kv', '.'), ('..\\src\\database.db', '.'), ('..\\src\\logo.png', '.')],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Amber Ocean',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Amber Ocean')

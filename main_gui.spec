# -*- mode: python -*-

block_cipher = None


a = Analysis(['main_gui.py'],
             pathex=['F:\\pict\\gif_blue'],
             binaries=[],
             datas=[('F:\git\pack\opencv_videoio_ffmpeg411.dll','.')],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main_gui',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False,
          icon = 'F:\git\pack\Co.ico' )

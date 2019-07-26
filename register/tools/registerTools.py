import winreg

REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

def set_reg( name, value ):
  winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
  registry_key = winreg.OpenKey( winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE )
  winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
  winreg.CloseKey( registry_key )
  return True
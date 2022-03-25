class Yin: pass
class Yang:
    def _del_(self):
        print("Yang destruido")

yin = Yin()
yang = Yang()
yin.yang = yang

print(yang)
print(yang is yin.yang)
del(yang)
print("?")


# __del__ no era accesible devido a que era privado por lo que se printeaba después. Al ya no ser privado, se ejecuta en orden.
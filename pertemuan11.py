#Nama   : Rizka Nurul Septiana Hakim
#NIM    : 20051397025
#Kelas  : 2020A
#Prodi  : D4 Manajemen Informatika

#memanggil openGL untuk menampilkan gambar hasil perhitungan algoritma bresenham
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initFun():
    #membersihkan background layar dan memberikan warna
    glClearColor(1.0,1.0,1.0,0.0)
    #menentukan warna garis
    glColor3f(128.0,0.0, 0.0)
    #spesifikasikan diameter dari pixel yang akan digambar
    glPointSize(5.0)
    #merubah status openGL ke mode proyeksi (transformasi)
    glMatrixMode(GL_PROJECTION)
    #memanggil matriks identitas dan mereset project matrix sebelumnya
    glLoadIdentity()
    #set origin dari grid dan ukurannya
    gluOrtho2D(0.0,640.0,0.0,480.0)
    
def AlgBresenham():
    #tentukan titik awal dan akhir
    x1 = 20
    y1 = 20
    x2 = 500
    y2 = 400
    x = x1
    y = y1

    #hitung dx dan dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    #hitung p (parameter)
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)
    
    #tentukan titik awal dan akhir
    if (x1 > x2):
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    

    #memilih mode point
    glBegin(GL_POINTS)
    #menentukan titik-titik
    glVertex2i(x, y)

    #perulangan untuk menggambar titik-titik (looping)
    while (x < xend):
        x = x+1
        if (p < 0):
            p += duady
        else:
            if (y1 > y2):
                y = y-1
            else:
                y = y+1
            p += duadydx
        glVertex2i(x, y)

    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()
    #inisialisasi pembuatan window
    glutInitWindowSize(640,480)
    #menampilkan tulisan ke window
    glutCreateWindow("Algoritma Bresenham - Grafika Komputer")
    #inisialisasi modus display untuk memanggil fungsi
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutDisplayFunc(AlgBresenham)
    initFun()
    #sintaks untuk me-looping atau mengulang fungsi/method main
    glutMainLoop()
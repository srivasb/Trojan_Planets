/* 
 Algoritmo PEFRL: Position-Extended-ForestRuth-Like 4th order

 Problema: Simular el moviminto de Dos Planeta
 Planet[1]: Jupyter
 Planet[0]: Sun
 
    razon radios: R0=10*R1

 Sistema rotado:
  [x' y']T = R(theta) [x t]
  theta = omega*t

 Metodo: Clase Colisionador

 Constantes: Encoding "UTF 8" 
    CEBE = xi
    CE9B = lambda
    CF87 = chi
*/

#include <iostream>
#include <cmath>
#include "Vector.h"
using namespace std;

// --- Declaracion de constantes
const int N=2; // num. de cuerpos
const double G=1.0;
const double xi=0.1786178958448091e00; 
const double lambda=-0.2123418310626054e00 ;
const double chi=-0.6626458266981849e-1 ;

const double Coeficiene1 = (1.0-2.0*lambda)/2.0 ;
const double Coeficiente2 = 1.0-2.0*(chi+xi) ;

// --- Declarar Clases
class Cuerpo;
class Colisionador;

// --------- Interfase e Implementar Clases ------

// Clase Cuerpo
class Cuerpo{
public:
  vector3D r,V,F; double m,R;
public:
  void Inicie(double x0,double y0,double Vx0,double Vy0,double m0,double R0);
  void BorreFuerza(void){F.cargue(0,0,0);};
  void AdicioneFuerza(vector3D F0){F+=F0;};
  void Mueva_r(double dt,double coeficiente);
  void Mueva_v(double dt,double coeficiente);
  void Dibujese(void);
  double Getx(void){return r.x();}; //inline
  double Gety(void){return r.y();}; //inline
  double Getz(void){return r.z();}; //inline
  friend class Colisionador; // Colisionador Class Uses All variables from Cuerpo
};
void Cuerpo::Inicie(double x0,double y0,double Vx0,double Vy0,double m0, double R0){
  r.cargue(x0,y0,0); V.cargue(Vx0,Vy0,0); m=m0; R=R0; 
} 
void Cuerpo::Mueva_r(double dt,double coeficiente){
    r+=V*(coeficiente*dt);
}
void Cuerpo::Mueva_v(double dt, double coeficiente){
    V+=F*(coeficiente*dt/m);
}
// Colisionador
class Colisionador{
private: 
public: 
  void calculefuerzas(Cuerpo * Planeta);
  void CalculeFuerzaEntre(Cuerpo & Planeta1, Cuerpo & Planeta2);
};
void Colisionador::calculefuerzas(Cuerpo * Planeta){
  int i, j;
  // Borrar Todas las Fuerzas
  for(i=0; i<N; i++){
     Planeta[i].BorreFuerza();
     }
  // Calcular fuerzas entre pares de planetas
  for(i=0;i<N;i++)
    for(j=i+1;j<N;j++)
      CalculeFuerzaEntre(Planeta[i],Planeta[j]);
}
void Colisionador::CalculeFuerzaEntre(Cuerpo & Planeta1, Cuerpo & Planeta2){
  vector3D r21=Planeta2.r-Planeta1.r;
  double aux=G*Planeta2.m*Planeta1.m*pow(norma2(r21),-1.5);
  vector3D F1=r21*aux;
  Planeta1.AdicioneFuerza(F1);   Planeta2.AdicioneFuerza(F1*(-1)); 
}


//-------------- Funciones de Animacion ----------
void Cuerpo::Dibujese(void){
  cout<<" , "<<r.x()<<"+"<<R<<"*cos(t),"<<r.y()<<"+"<<R<<"*sin(t)";
}
void InicieAnimacion(void){
  cout<<"set terminal gif animate"<<endl; 
  cout<<"set output 'b.gif'"<<endl;
  cout<<"unset key"<<endl;
  cout<<"set xrange[-1050:1050]"<<endl;
  cout<<"set yrange[-1050:1050]"<<endl;
  cout<<"set size ratio -1"<<endl;
  cout<<"set parametric"<<endl;
  cout<<"set trange [0:7]"<<endl;
  cout<<"set isosamples 12"<<endl;  
}
void InicieCuadro(void){
    cout<<"plot 0,0 ";
}
void TermineCuadro(void){
    cout<<endl;
}


//-----------  Programa Principal --------------  
int main(void){
  int i;
  Cuerpo Planeta[N];
  Colisionador Newton; 

  double r=1000, m0=1047, m1=1;
  double R1=2.0, R0=10.0*R1;
  double M=m1+m0, Mu=(m0*m1)/M; 
  double x0=-m1*r/M, x1=r+x0;
  double omega=sqrt(G*M*pow(r,-3.0)), T= 2*M_PI/omega;
  double V0=omega*x0, V1=omega*x1;

  double xrot, yrot, theta;

  double t,tdibujo,tcuadro=T/100,dt=0.01;
  double tmax=20.2*T;

  //Dibujar
  // InicieAnimacion();

  //---------------(x0,y0,Vx0,Vy0,m0,r)
  Planeta[0].Inicie(x0, 0, 0,V0, m0,R0); // Sol
  Planeta[1].Inicie(x1, 0, 0,V1, m1,R1); // Jupiter

  for(t=0,tdibujo=0 ; t<tmax ; t+=dt,tdibujo+=dt){
    
    if(tdibujo>tcuadro){
    //   InicieCuadro();
    //   for(int k=0; k<N; k++) Planeta[k].Dibujese();
    //   TermineCuadro();
    // cout<<Planeta[0].Getx()<<" "<<Planeta[0].Gety()<<" "<<Planeta[1].Getx()<<" "<<Planeta[1].Gety()<<endl;

    theta=omega*t ;
    xrot =  Planeta[1].Getx()*cos(theta)+Planeta[1].Gety()*sin(theta);
    yrot = -Planeta[1].Getx()*sin(theta)+Planeta[1].Gety()*cos(theta);
    cout<<xrot<<" "<<yrot<<endl ;

    tdibujo=0;
    }
    // PEFRL algoritmo
    for(i=0;i<N;i++)Planeta[i].Mueva_r(dt,xi); 
    Newton.calculefuerzas(Planeta);
    for(i=0;i<N;i++)Planeta[i].Mueva_v(dt,Coeficiene1);
    for(i=0;i<N;i++)Planeta[i].Mueva_r(dt,chi);
    Newton.calculefuerzas(Planeta);
    for(i=0;i<N;i++)Planeta[i].Mueva_v(dt,lambda);
    for(i=0;i<N;i++)Planeta[i].Mueva_r(dt,Coeficiente2);
    Newton.calculefuerzas(Planeta); 
    for(i=0;i<N;i++)Planeta[i].Mueva_v(dt,lambda);
    for(i=0;i<N;i++)Planeta[i].Mueva_r(dt,chi);
    Newton.calculefuerzas(Planeta); 
    for(i=0;i<N;i++)Planeta[i].Mueva_v(dt,Coeficiene1);
    for(i=0;i<N;i++)Planeta[i].Mueva_r(dt,xi); 
  }
  return 0;
}
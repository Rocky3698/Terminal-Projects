// #include <iostream>
// #include <cmath>
// #include <vector>
// using namespace std;
// vector<double> vec1;
// vector<char> vec2;

// void Linear_Equation()
// {
//     double a1, a2, b1, b2, c1, c2;
//     cout << "a1x+b1y=c1" << endl
//          << "a2x+b2y=c2" << endl;
//     cout << "Enter a1,b1,c1" << endl;
//     cin >> a1 >> b1 >> c1;

//     cout << "Enter a2,b2,c2" << endl;
//     cin >> a2 >> b2 >> c2;
//     cout << endl
//          << "X = " << ((b2 * c1) - (b1 * c2)) / ((a1 * b2) - (a2 * b1)) << endl
//          << "Y = " << ((a1 * c2) - (a2 * c1)) / ((a1 * b2) - (a2 * b1)) << endl
//          << endl;
// }

// void Quadratic_Equation()
// {
//     cout << "ax^2 + bx + c = 0" << endl;
//     double a, b, c;
//     cout << "Enter a,b,c" << endl;

//     cin >> a >> b >> c;
//     cout << endl
//          << "X1 = " << (-b + sqrt((b * b) - (4 * a * c))) / (2 * a) << endl
//          << "X2 = " << (-b - sqrt((b * b) - (4 * a * c))) / (2 * a) << endl
//          << endl;
// }

// void Mass()
// {
//     cout << "Enter present unit of Mass" << endl
//          << "Enter 'G' for Grams" << endl
//          << "Enter 'K' for Kilogram" << endl;
//     while (true)
//     {
//         char punit, cunit;
//         cin >> punit;
//         if (punit == 'g' || punit == 'G')
//         {
//             double grams;
//             cout << "Enter Mass" << endl;

//             cin >> grams;
//             cout << grams / 1000 << "Kg" << endl
//                  << endl;
//             break;
//         }
//         else if (punit == 'k' || punit == 'K')
//         {
//             double kg;
//             cin >> kg;
//             cout << kg * 1000 << "g" << endl
//                  << endl;
//             break;
//         }

//         else
//             cout << "Please Enter unit as form of G or K" << endl;
//     }
// }

// void Lenght()
// {
//     double mm, cm, m, km;
//     cout << "Enter present unit of Lenght" << endl
//          << "Enter 'L' for Milimeter" << endl
//          << "Enter 'C' for Centimeter" << endl
//          << "Enter 'M' for Meter" << endl
//          << "Enter 'K' for kilometer" << endl;

//     while (true)
//     {
//         char punit, cunit;

//         cin >> punit;
//         if (punit == 'l' || punit == 'L')
//         {
//             cout << "Enter the Lenght" << endl;
//             cin >> mm;
//             cout << "Enter Coversion unit C or M" << endl;
//             cin >> cunit;
//             if (cunit == 'c' || cunit == 'C')
//             {

//                 cout << mm * 0.1 << "cm" << endl
//                      << endl;
//             }
//             else if (cunit == 'm' || cunit == 'M')
//             {

//                 cout << mm * 0.001 << "m" << endl
//                      << endl;
//             }
//             break;
//         }

//         else if (punit == 'C' || punit == 'c')
//         {
//             cout << "Enter the Lenght" << endl;

//             cin >> cm;
//             cout << "Enter coversion unit M or L " << endl;
//             cin >> cunit;
//             if (cunit == 'm' || cunit == 'M')
//             {
//                 cout << cm * 0.01 << "m" << endl
//                      << endl;
//             }
//             else if (cunit == 'l' || cunit == 'L')
//             {

//                 cout << cm * 10 << "mm" << endl
//                      << endl;
//             }

//             break;
//         }

//         else if (punit == 'm' || punit == 'M')
//         {
//             cout << "Enter the Lenght" << endl;
//             cin >> m;
//             cout << "Enter Coversion form C or K " << endl;
//             cin >> cunit;
//             if (cunit == 'c' || cunit == 'C')
//             {
//                 cout << m * 100 << "cm" << endl
//                      << endl;
//             }
//             else if (cunit == 'k' || cunit == 'K')
//             {
//                 cout << m * 0.001 << "km" << endl
//                      << endl;
//             }
//             break;
//         }

//         else if (punit == 'k' || punit == 'K')
//         {
//             cout << "Enter the Lenght" << endl;
//             cin >> km;
//             cout << "Enter Coversion form C or M " << endl;
//             cin >> cunit;
//             if (cunit == 'c' || cunit == 'C')
//             {
//                 cout << km * 100000 << "cm" << endl
//                      << endl;
//             }
//             else if (cunit == 'm' || cunit == 'M')
//             {
//                 cout << km * 1000 << "m" << endl
//                      << endl;
//             }
//             break;
//         }
//         else
//             cout << "Please Enter unit as form of C, F or K" << endl;
//     }
// }

// void Volume()
// {
//     cout << "Enter present unit of Volume" << endl
//          << "Enter 'M' for Milliliter" << endl
//          << "Enter 'L' for Liter" << endl;
//     while (true)
//     {
//         char punit, cunit;
//         double volume;
//         cin >> punit;
//         cout << "Enter Mass" << endl;
//         cin >> volume;
//         if (punit == 'm' || punit == 'M')
//         {
//             cout << volume * 0.001 << "L" << endl
//                  << endl;
//             break;
//         }
//         else if (punit == 'l' || punit == 'L')
//         {
//             cout << volume * 1000 << "ml" << endl
//                  << endl;
//             break;
//         }

//         else
//             cout << "Please Enter unit as form of M or L" << endl;
//     }
// }

// void Time()
// {
//     cout << "Upcoming..." << endl;
// }

// void Speed()
// {
//     cout << "Enter present unit of speed" << endl
//          << "Enter 'M' m/s" << endl
//          << "Enter 'K' for km/h" << endl;
//     while (true)
//     {
//         char punit, cunit;
//         cin >> punit;
//         double speed;
//         if (punit == 'm' || punit == 'M')
//         {

//             cout << "Enter Speed" << endl;

//             cin >> speed;
//             cout << speed * 3.6 << "km/h" << endl
//                  << endl;
//             break;
//         }
//         else if (punit == 'k' || punit == 'K')
//         {

//             cin >> speed;
//             cout << speed / 3.6 << "m/s" << endl
//                  << endl;
//             break;
//         }

//         else
//             cout << "Please Enter unit as form of M or K" << endl;
//     }
// }

// void Temperature()
// {
//     double c, f, k;
//     char punit, cunit;
//     cout << "Enter present unit of temperature" << endl
//          << "C for celcious" << endl
//          << "F for farenhite" << endl
//          << "K for kelvin" << endl;

//     while (true)
//     {
//         cin >> punit;

//         if (punit == 'C' || punit == 'c')
//         {
//             cout << "Enter the Tempreture" << endl;

//             cin >> c;
//             cout << "Enter Coversion form F or K " << endl;
//             cin >> cunit;
//             if (cunit == 'F' || cunit == 'f')
//             {
//                 f = 1.8 * c + 32;
//                 cout << "F = " << f << endl
//                      << endl;
//             }
//             else if (cunit == 'K' || cunit == 'k')
//             {
//                 k = c + 273;
//                 cout << "K = " << k << endl
//                      << endl;
//             }

//             break;
//         }
//         else if (punit == 'F' || punit == 'f')
//         {
//             cout << "Enter the Tempreture" << endl;
//             cin >> f;
//             cout << "Enter Coversion form C or K " << endl;
//             cin >> cunit;
//             if (cunit == 'K' || cunit == 'k')
//             {
//                 k = 5 * (f - 32) / 9 + 273;
//                 cout << "K = " << k << endl
//                      << endl;
//             }
//             else if (cunit == 'C' || cunit == 'c')
//             {
//                 c = (f - 32) * (5 / 9);
//                 cout << "C = " << c << endl
//                      << endl;
//             }
//             break;
//         }
//         else if (punit == 'K' || punit == 'k')
//         {
//             cout << "Enter the Tempreture" << endl;
//             cin >> k;
//             cout << "Enter Coversion form F or C " << endl;
//             cin >> cunit;
//             if (cunit == 'C' || cunit == 'c')
//             {
//                 c = k - 273;
//                 cout << "C = " << c << endl
//                      << endl;
//             }
//             else if (cunit == 'F' || cunit == 'f')
//             {
//                 f = ((k - 273) * 9 / 5) + 32;
//                 cout << "F = " << f << endl
//                      << endl;
//             }
//             break;
//         }
//         else
//             cout << "Please Enter unit as form of C, F or K" << endl;
//     }
// }

// void Number_System()
// {
//     cout << "Upcoming..." << endl;
// }

// void Add()
// {
//     double elements, result;
//     char signs;
//     cout << "Give input without space.\nPress '=' sign & 'Enter' to get answer." << endl;
//     while (true)
//     {
//         cin >> elements;
//         vec1.push_back(elements);
//         cin >> signs;
//         vec2.push_back(signs);
//         if (signs == '=')
//             break;
//     }
//     result = vec1[0];
//     for (int i = 0; i < vec1.size(); i++)
//     {

//         if (vec2[i] == '+')
//         {
//             result += vec1[i + 1];
//         }
//         else if (vec2[i] == '-')
//         {
//             result -= vec1[i + 1];
//         }
//     }
//     cout << result << endl;
// }

// void Percentage()
// {
//     double n1, n2;
//     cout << "Enter total number" << endl;
//     cin >> n1;
//     cout << "How many percentage you want to know" << endl;
//     cin >> n2;
//     cout << "percentage= " << n1 * n2 / 100 << "%" << endl;
// }

// void Divid()
// {
//     double num1, num2;
//     cout << "Enter dividen" << endl;
//     cin >> num1;
//     cout << "Enter divisor" << endl;
//     cin >> num2;
//     cout << "Quotient= " << num1 / num2 << endl;
// }

// void Multiply()
// {
//     int num;
//     double result = 1, multi;
//     cout << "Enter how many number you want to multiply" << endl;
//     cin >> num;
//     cout << "Enter multipliers" << endl;
//     while (num--)
//     {
//         cin >> multi;
//         result *= multi;
//     }
//     cout << "Product= " << result << endl;
// }


// int main()
// {

//     while (true)
//     {
//         int mood;
//         cout << "What you want to do?" << endl;
//         cout << "Enter '1' for basic calculation" << endl
//              << "Enter '2'for solve Equation" << endl
//              << "Enter '3' for coversion" << endl
//              << "Enter '0' for exit" << endl;
//         cin >> mood;
//         if (mood == 0)
//             break;
//         switch (mood)
//         {
//         case 1:
//         //Basic calculation.
//             char sign;
//             cout << "Enter '+' for add and subtract.\nEnter '*' for multiply.\nEnter '/' for divide.\nEnter '%' for find Percentage.\n"
//                  << endl;
//             cin >> sign;
//             switch (sign)
//             {

//             case '+':
//                 Add();
//                 break;

//             case '*':
//                 Multiply();
//                 break;

//             case '/':
//                 Divid();
//                 break;

//             case '%':
//                 Percentage();
//                 break;

//             default:
//                 cout << "Error! Something was wrong." << endl;

//                 break;
//             }

//             break;
//         case 2:
//             // Equations
//             int type;
//             cout << "Enter '1' for Linear Equation" << endl
//                  << "Enter '2' for Quadratic Equation" << endl;
//             cin >> type;

//             switch (type)
//             {

//             case 1:
//                 Linear_Equation();
//                 break;
//             case 2:
//                 Quadratic_Equation();
//                 break;
//             default:
//                 cout << "Error!" << endl;
//                 break;
//             }
//             break;

//         case 3:
//             // Conversions
//             cout << "Enter '1' for Mass" << endl
//                  << "Enter '2' for Lenght" << endl
//                  << "Enter '3' for Volume" << endl
//                  << "Enter '4' for Time" << endl
//                  << "Enter '5' for Speed" << endl
//                  << "Enter '6' for Temperature" << endl
//                  << "Enter '7' for Number System" << endl;
//             int cmood;
//             cin >> cmood;
//             switch (cmood)
//             {
//             case 1:
//                 Mass();
//                 break;

//             case 2:
//                 Lenght();
//                 break;

//             case 3:
//                 Volume();
//                 break;

//             case 4:
//                 Time();
//                 break;

//             case 5:
//                 Speed();
//                 break;

//             case 6:
//                 Temperature();
//                 break;

//             case 7:
//                 Number_System();
//                 break;

//             default:
//                 cout << "Error!" << endl;
//                 break;
//             }

//             break;

//         default:
//             cout << "Error! Something was wrong" << endl
//                  << endl;

//             break;
//         }
//     }

//     return 0;
// }
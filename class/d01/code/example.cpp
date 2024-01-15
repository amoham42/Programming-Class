#include <boost/multiprecision/cpp_dec_float.hpp>
#include <boost/math/constants/constants.hpp>
#include <iostream>
#include <chrono>

using boost::multiprecision::cpp_dec_float_100;
using namespace std::chrono;

int main() {
    auto start = high_resolution_clock::now();

    cpp_dec_float_100 pi = boost::math::constants::pi<cpp_dec_float_100>();

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    std::cout.precision(1000);
    std::cout << "Pi to 1000 digits:\n" << pi << std::endl;
    std::cout << "Time taken: " << duration.count() << " microseconds" << std::endl;

    return 0;
}

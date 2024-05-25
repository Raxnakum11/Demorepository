#include <iostream>
#include <string>

class SOLID_CARBon {
protected:
    std::string diamond_or_graphite;
    std::string o_name;

public:
    SOLID_CARBon(std::string d_or_g, std::string owner_name) : diamond_or_graphite(d_or_g), o_name(owner_name) {}

    void display() {
        std::cout << "Type: " << diamond_or_graphite << std::endl;
        std::cout << "Owner: " << o_name << std::endl;
    }
};

class DIAMOND : public SOLID_CARBon {
private:
    int carat;
    std::string color;

public:
    DIAMOND(std::string d_or_g, std::string owner_name, int c, std::string col) : SOLID_CARBon(d_or_g, owner_name), carat(c), color(col) {}

    void display() {
        SOLID_CARBon::display();
        std::cout << "Carat: " << carat << std::endl;
        std::cout << "Color: " << color << std::endl;
    }
};

int main() {
    DIAMOND* diamond_ptr = new DIAMOND("Diamond", "John Doe", 5, "White");

    diamond_ptr->display();

    delete diamond_ptr;

    return 0;
}

import './Home.css';
import ProductCard from "../components/ProductCard";

const Home = () => {
    const products = [
        {
            id:1,
            name:'asdf',
            price:200,
            picture:'asdf.png',
            desc:'asdf',
        },
        {
            id:2,
            name:'colgate',
            price:200,
            picture:'asdf.png',
            desc:'asdf',
        },
        {
            id:3,
            name:'asdf',
            price:200,
            picture:'asdf.png',
            desc:'asdf',
        },
        {
            id:4,
            name:'asdf',
            price:200,
            picture:'asdf.png',
            desc:'asdf',
        }
    ]

    return (
        <div className="container">
            <h1>Products</h1>
            <div className="row products">
                {products.map((this_product) => (
                    <ProductCard key={this_product.id} product={this_product}/>
                ) )}
            </div>
            
        </div>
    );
};

export default Home;
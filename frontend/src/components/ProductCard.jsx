import './ProductCard.css';

const ProductCard = ({ product }) => {

    return (
        <div className="card col-12 col-md-6 col-lg-4">
            <img src="{product.picture}" className="card-img-top" alt="..."/>
                <div className="card-body">
                    <h5 className="card-title">{product.name}</h5>
                    <p className="card-text">
                        <small class="text-body-secondary">
                            Rs.{product.price}
                        </small>
                    </p>
                </div>
        </div>
    );
};

export default ProductCard;



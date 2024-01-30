import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Allrestaurants() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/restaurants")
      .then((r) => r.json())
      .then(setRestaurants);
    console.log(restaurants);
  }, []);

  function handleDelete(id) {
    fetch(`http://127.0.0.1:5555/restaurants/${id}`, {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setRestaurants((restaurants) =>
          restaurants.filter((restaurant) => restaurant.id !== id)
        );
      }
    });
  }

  return (
    
    <section style={{ backgroundColor: "grey" }}>
      <h1 style={{ color: "Orange" }}>Top Pizza Restaurants in town</h1>
      <ol style={{ marginRight: 1000 }}>
        {restaurants.map((restaurant) => (
          <li
            key={restaurant.id}
            style={{ borderRadius: "5px", padding: "25px", border: "1px" }}
          >
            <Link
              to={`/restaurants/${restaurant.id}`}
              style={{ borderRadius: 50 }}
            >
              {restaurant.name}
            </Link>
            <button
              onClick={() => handleDelete(restaurant.id)}
              style={{ backgroundColor: "red" }}
            >
              delete Restaurant
            </button>
          </li>
        ))}
      </ol>
    </section>
  );
}
export default Allrestaurants;

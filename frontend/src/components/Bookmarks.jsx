import React, { useState, useEffect } from "react";
import apiClient from "../api";
import { useAuth } from "../context/AuthContext";

const Bookmarks = () => {
  const { logout } = useAuth();
  const [bookmarks, setBookmarks] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchBookmarks = async () => {
      try {
        const response = await apiClient.get("/bookmarks/");
        setBookmarks(response.data);
      } catch (err) {
        setError("Failed to fetch bookmarks. You might need to log in again.");
        console.error(err);
      }
    };

    fetchBookmarks();
  }, []);

  return (
    <div>
      <button onClick={logout} style={{ float: "right" }}>
        Logout
      </button>
      <h2>My Bookmarks</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {bookmarks.length > 0 ? (
        <ul>
          {bookmarks.map((bookmark) => (
            <li key={bookmark.id}>
              <a href={bookmark.url} target="_blank" rel="noopener noreferrer">
                {bookmark.title}
              </a>
              <p>{bookmark.description}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No bookmarks found.</p>
      )}
    </div>
  );
};
export default Bookmarks;

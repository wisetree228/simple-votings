import React from 'react';

export const Footer = () => {
  return (
    <footer className="bg-gray-800 py-4 px-6 mt-auto">
      <div className="container mx-auto text-center text-gray-400">
        <p>&copy; {new Date().getFullYear()} SimpleVotes. All rights reserved.</p>
      </div>
    </footer>
  );
};
import React from 'react';
import { Button } from './Button';

export const MainContent = () => {
  return (
    <div className="flex flex-col sm:flex-row gap-4">
      <Button variant="primary">Register</Button>
      <Button variant="secondary">Sign In</Button>
    </div>
  );
};
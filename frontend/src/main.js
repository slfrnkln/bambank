import React from 'react';
import { Routes, Route } from 'react-router-dom'

import LogIn  from './pages/login';
import CreateAccount from './pages/create_account';
// import Balance from './pages/balance';

const Main = () => {
    return (
        <Routes>
            <Route exact path='/' element={<LogIn />}></Route>
            <Route exact path='/account' element={<CreateAccount />}></Route>
            {/* <Route exact path='/account/balance' component={Balance}></Route> */}
        </Routes>
    )
}

export default Main;
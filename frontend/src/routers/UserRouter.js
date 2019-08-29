import React from 'react';
import { Route, Switch } from 'react-router-dom';

import UserUploadPage from '../components/pages/user/UserUploadPage';
import UserProjectPage from '../components/pages/user/UserProjectPage';
import SettingsRouter from './SettingsRouter';

import LayoutRoute from './LayoutRoute';
import UserLayout from '../components/fixed/UserLayout';
import NotFound from '../components/pages/public/NotFound';

export default ({ match }) => {
  return (
    <Switch>
      <LayoutRoute
        exact
        path={`${match.url}/upload`}
        layout={UserLayout}
        component={UserUploadPage}
      />
      <LayoutRoute
        exact
        path={`${match.url}/projects`}
        layout={UserLayout}
        component={UserProjectPage}
      />
      <Route path={`${match.url}/settings`} component={SettingsRouter} />
      <Route component={NotFound} />
    </Switch>
  );
};

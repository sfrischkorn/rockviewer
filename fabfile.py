# Define the Fabric script
# globals
config.project_name = 'rockviewer'
# environments
def local():
    "Use the local virtual server"
    config.hosts = ['172.16.142.130']
    config.path = '~/www/rockviewer'
    config.user = 'shane'
    config.virtualhost_path = "/"
# tasks
def test():
    "Run the test suite and bail out if it fails"
    local("cd $(project_name); python manage.py test", fail="abort")
def setup():
    """
    Setup a fresh virtualenv as well as a few useful directories, then run
    a full deployment
    """
    require('hosts', provided_by=[local])
    require('path')
    sudo('aptitude install -y python-setuptools')
    sudo('easy_install pip')
    sudo('pip install virtualenv')
    sudo('aptitude install -y apache2')
    sudo('aptitude install -y libapache2-mod-wsgi')
    # we want rid of the defult apache config
    sudo('cd /etc/apache2/sites-available/; a2dissite default;')
    run('mkdir -p $(path); cd $(path); virtualenv .;')
    run('cd $(path); mkdir releases; mkdir shared; mkdir packages;', fail='ignore')
    deploy()
def deploy():
    """
    Deploy the latest version of the site to the servers, install any
    required third party modules, install the virtual host and 
    then restart the webserver
    """
    require('hosts', provided_by=[local])
    require('path')
    import time
    config.release = time.strftime('%Y%m%d%H%M%S')
    upload_tar_from_git()
    install_requirements()
    install_site()
    symlink_current_release()
    migrate()
    restart_webserver()
def deploy_version(version):
    "Specify a specific version to be made live"
    require('hosts', provided_by=[local])
    require('path')
    config.version = version
    run('cd $(path); rm releases/previous; mv releases/current releases/previous;')
    run('cd $(path); ln -s $(version) releases/current')
    restart_webserver()
def rollback():
    """
    Limited rollback capability. Simple loads the previously current
    version of the code. Rolling back again will swap between the two.
    """
    require('hosts', provided_by=[local])
    require('path')
    run('cd $(path); mv releases/current releases/_previous;')
    run('cd $(path); mv releases/previous releases/current;')
    run('cd $(path); mv releases/_previous releases/previous;')
    restart_webserver()    
# Helpers. These are called by other functions rather than directly
def upload_tar_from_git():
    require('release', provided_by=[deploy, setup])
    "Create an archive from the current Git master branch and upload it"
    local('git archive --format=tar master | gzip > $(release).tar.gz')
    run('mkdir $(path)/releases/$(release)')
    put('$(release).tar.gz', '$(path)/packages/')
    run('cd $(path)/releases/$(release) && tar zxf ../../packages/$(release).tar.gz')
    local('rm $(release).tar.gz')
def install_site():
    "Add the virtualhost file to apache"
    require('release', provided_by=[deploy, setup])
    sudo('cd $(path)/releases/$(release); cp $(project_name)$(virtualhost_path)$(project_name) /etc/apache2/sites-available/')
    sudo('cd /etc/apache2/sites-available/; a2ensite $(project_name)') 
def install_requirements():
    "Install the required packages from the requirements file using pip"
    require('release', provided_by=[deploy, setup])
    run('cd $(path); pip install -E . -r ./releases/$(release)/requirements.txt')
def symlink_current_release():
    "Symlink our current release"
    require('release', provided_by=[deploy, setup])
    run('cd $(path); rm releases/previous; mv releases/current releases/previous;', fail='ignore')
    run('cd $(path); ln -s $(release) releases/current')
def migrate():
    "Update the database"
    require('project_name')
    run('cd $(path)/releases/current/$(project_name);  ../../../bin/python manage.py syncdb --noinput')
def restart_webserver():
    "Restart the web server"
    sudo('/etc/init.d/apache2 restart')
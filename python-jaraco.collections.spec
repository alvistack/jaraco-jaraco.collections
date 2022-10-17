# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-jaraco.collections
Epoch: 100
Version: 3.5.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Collection objects similar to those in stdlib by jaraco
License: MIT
URL: https://github.com/jaraco/jaraco.collections/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Models and classes to supplement the stdlib 'collections' module.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-jaraco.collections
Summary: Collection objects similar to those in stdlib by jaraco
Requires: python3
Requires: python3-jaraco.classes
Requires: python3-jaraco.text
Provides: python3-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python3dist(jaraco.collections) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jaraco.collections) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jaraco.collections) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-jaraco.collections
Models and classes to supplement the stdlib 'collections' module.

%files -n python%{python3_version_nodots}-jaraco.collections
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-jaraco.collections
Summary: Collection objects similar to those in stdlib by jaraco
Requires: python3
Requires: python3-jaraco.classes
Requires: python3-jaraco.text
Provides: python3-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python3dist(jaraco.collections) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jaraco.collections) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jaraco.collections) = %{epoch}:%{version}-%{release}

%description -n python3-jaraco.collections
Models and classes to supplement the stdlib 'collections' module.

%files -n python3-jaraco.collections
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-jaraco-collections
Summary: Collection objects similar to those in stdlib by jaraco
Requires: python3
Requires: python3-jaraco-classes
Requires: python3-jaraco-text
Provides: python3-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python3dist(jaraco.collections) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jaraco.collections) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jaraco.collections = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jaraco.collections) = %{epoch}:%{version}-%{release}

%description -n python3-jaraco-collections
Models and classes to supplement the stdlib 'collections' module.

%files -n python3-jaraco-collections
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog

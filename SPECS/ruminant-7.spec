%global service_name %{name}

Name:             %{name}
Version:          %{ver}
Release:          %{rel}%{?dist}
Summary:          ruminant for RHEL/CENTOS %{os_rel}
BuildArch:        %{arch}
Group:            Application/ETL
License:          MIT
URL:              https://github.com/unprofession-al/bpmon
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source1:        bpmon.bin

%define appdir /usr/bin/

%description
netmgmt for RHEL/CENTOS %{os_rel}

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{appdir}
%{__install} -p -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/%{appdir}/ruminant

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) %{appdir}/ruminant

%changelog
* Wed Mar 15 2017 Daniel Menet <daniel.menet@swisstxt.ch> - 1-1
Initial creation
